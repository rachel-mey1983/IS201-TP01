
#define WIN32_LEAN_AND_MEAN
#include <Python.h>
#include <windows.h>

int
PyMOL_Main(int argc, wchar_t **argv)
{
    PyStatus status;
    PyConfig config;

    PyConfig_InitPythonConfig(&config);
    status = PyConfig_SetArgv(&config, argc, argv);
    if (PyStatus_Exception(status)) {
        goto fail;
    }
    config.parse_argv = 0;
    status = PyConfig_SetString(&config, &config.run_module, L"pymol");
    if (PyStatus_Exception(status)) {
        goto fail;
    }
    status = Py_InitializeFromConfig(&config);
    if (PyStatus_Exception(status)) {
        goto fail;
    }
    PyConfig_Clear(&config);
    return Py_RunMain();

fail:
    PyConfig_Clear(&config);
    if (PyStatus_IsExit(status)) {
        return status.exitcode;
    }
    assert(PyStatus_Exception(status));
    Py_ExitStatusException(status);
    return 0;
}

int WINAPI wWinMain(
    HINSTANCE hInstance,
    HINSTANCE hPrevInstance,
    LPWSTR lpCmdLine,
    int nCmdShow
)
{
    return PyMOL_Main(__argc, __wargv);
}
