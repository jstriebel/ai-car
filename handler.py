from abc import ABC, abstractmethod

class Handler(ABC):
	@abstractmethod
	def handle(self, request):
		pass

	@abstractmethod
	def __enter__(self):
		pass

	@abstractmethod
    def __exit__(self, exit_type, value, traceback):
        pass
