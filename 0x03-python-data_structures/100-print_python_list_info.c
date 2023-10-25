#include <Python.h>

/**
 * print_python_list_info - prints basic info about Python lists
 * @p: python object param
 */
void print_python_list_info(PyObject *p)
{
	int i;
	int size = Py_SIZE(p);

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %li\n", ((PyListObject *)p)->allocated);

	for (i = 0, i < size; i++)
		printf("Element %d: %s\n", i,
				Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
