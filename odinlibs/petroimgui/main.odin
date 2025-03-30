package petroimgui

// This is an example of using the bindings with GLFW and OpenGL 3.
// For a more complete example with comments, see:
// https://github.com/ocornut/imgui/blob/docking/examples/example_glfw_opengl3/main.cpp
// Based on the above at tag `v1.91.1-docking` (d8c98c)

DISABLE_DOCKING :: #config(DISABLE_DOCKING, false)

import "core:os"
import "core:fmt"
import im "shared:imgui"
import "shared:imgui/imgui_impl_glfw"
import "shared:imgui/imgui_impl_opengl3"

import "vendor:glfw"
import gl "vendor:OpenGL"
import ls "shared:lasio"

main :: proc() {
    assert(cast(bool)glfw.Init())
    defer glfw.Terminate()

    glfw.WindowHint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.WindowHint(glfw.CONTEXT_VERSION_MINOR, 2)
    glfw.WindowHint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    glfw.WindowHint(glfw.OPENGL_FORWARD_COMPAT, 1) // i32(true)

    window := glfw.CreateWindow(1280, 720, "Dear ImGui GLFW+OpenGL3 example", nil, nil)
    assert(window != nil)
    defer glfw.DestroyWindow(window)

    glfw.MakeContextCurrent(window)
    glfw.SwapInterval(2) // vsync

    gl.load_up_to(3, 2, proc(p: rawptr, name: cstring) {
        (cast(^rawptr)p)^ = glfw.GetProcAddress(name)
    })

    im.CHECKVERSION()
    im.CreateContext()
    defer im.DestroyContext()
    io := im.GetIO()
    io.ConfigFlags += {.NavEnableKeyboard, .NavEnableGamepad}
    when !DISABLE_DOCKING {
        io.ConfigFlags += {.DockingEnable}
        io.ConfigFlags += {.ViewportsEnable}

        style := im.GetStyle()
        style.WindowRounding = 0
        style.Colors[im.Col.WindowBg].w = 1
    }

    im.StyleColorsDark()

    imgui_impl_glfw.InitForOpenGL(window, true)
    defer imgui_impl_glfw.Shutdown()
    imgui_impl_opengl3.Init("#version 150")
    defer imgui_impl_opengl3.Shutdown()

    // here all the panels and data go.
    file_name: string = os.args[1]
    las_file, parsed_ok := ls.dummy_parser(file_name, 2016, allocator=context.allocator)
    defer {
        delete(las_file.file_name)
        delete(las_file.version.add)
        delete(las_file.curve_info.curves)
        delete(las_file.parameter_info.params)
        delete(las_file.other_info.info)
        delete(las_file.log_data.logs)
    }

    if parsed_ok != nil {
        fmt.printfln("Failed to parse the data, err: %v", parsed_ok)
    }

    las_panel: LAS_Panel
    las_panel_init(&las_panel, &las_file, "LAS Panel")


    for !glfw.WindowShouldClose(window) {
        glfw.PollEvents()

        imgui_impl_opengl3.NewFrame()
        imgui_impl_glfw.NewFrame()
        im.NewFrame()

        // menu_bar_height := im.GetFrameHeight()
        // im.SetNextWindowPos(im.Vec2{0, menu_bar_height})
        // im.SetNextWindowSize(im.GetIO().DisplaySize)
        // im.PushStyleVar(.WindowRounding, 0.0)
        // im.PushStyleVar(.WindowBorderSize, 0.0)
        // im.Begin("MainDockSpace", nil, {.NoTitleBar, .NoCollapse, .NoResize})
        // im.DockSpace(im.GetID("MainDockSpace"), im.Vec2{0, 0}, {.PassthruCentralNode})


        // ui code

        // viewport := im.GetMainViewport()
        // im.SetNextWindowPos({0,0}, .Appearing)
        // im.SetNextWindowSize(viewport.Size, .Appearing)

        im.ShowDemoWindow()
        if im.Begin("Window containing a quit button") {
            if im.Button("The quit button in question") {
                glfw.SetWindowShouldClose(window, true)
            }
        }
        im.End()

        // las_panel_render(&las_panel)
        // las_panel.rendered += 1

        im.Render()
        display_w, display_h := glfw.GetFramebufferSize(window)
        gl.Viewport(0, 0, display_w, display_h)
        gl.ClearColor(0, 0, 0, 1)
        gl.Clear(gl.COLOR_BUFFER_BIT)
        imgui_impl_opengl3.RenderDrawData(im.GetDrawData())

        when !DISABLE_DOCKING {
            backup_current_window := glfw.GetCurrentContext()
            im.UpdatePlatformWindows()
            im.RenderPlatformWindowsDefault()
            glfw.MakeContextCurrent(backup_current_window)
        }

        glfw.SwapBuffers(window)
    }
}
