# class FileContextManager:
#     def __init__(self, filename, mode):
#         print('FileContextManager initialized')

#         self.filename = filename
#         self.mode = mode
#         self.file = None

#     def __enter__(self):
#         print('entering the context manager')
#         self.file = open(self.filename, self.mode)
#         return self.file

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         self.file.close()
#         print('exiting the context manager')

# with FileContextManager('test_file.txt', 'w') as f:
#     f.write('in the main scope')




from contextlib import contextmanager


@contextmanager
def file(filename, mode):
  print('starting the context manager')
  f = open(filename, mode)
  yield f

  f.close()
  print('end')


filename = 'test.txt'
mode = 'w'
with file(filename, mode) as f:
  print('middle')
  