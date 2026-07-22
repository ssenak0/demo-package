import os
import sys
import cv2

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from sdks.novavision.src.media.image import Image
from sdks.novavision.src.base.capsule import Capsule
from sdks.novavision.src.helper.executor import Executor
from src.models.PackageModel import PackageModel

class ExecutorOne(Capsule):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.image_one = self.request.get_param("inputOne")
        self.method = self.request.get_param("demoDependentDropdown")
        
        if self.method == "OptionA":
            self.val_int = self.request.get_param("OptionAIntegerField")
            self.val_bool = self.request.get_param("OptionABooleanField")
        else:
            self.val_float = self.request.get_param("OptionBFloatField")
            self.val_str = self.request.get_param("OptionBStringField")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def process(self, img_one):
        gray_image = cv2.cvtColor(img_one, cv2.COLOR_BGR2GRAY)
        return gray_image

    def run(self):
        img_one = Image.get_frame(img=self.image_one, redis_db=self.redis_db)
        result = self.process(img_one.value)
        packageModel = self.request.model.dict()
        return packageModel

if "__main__" == __name__:
    Executor(sys.argv[1]).run()
