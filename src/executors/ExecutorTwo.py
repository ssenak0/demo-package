import os
import sys
import cv2

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from sdks.novavision.src.media.image import Image
from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor
from novavision.demo_package.models.PackageModel import PackageModel

class ExecutorTwo(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.image_two = self.request.get_param("inputImage2")
        self.image_three = self.request.get_param("inputImage3")
        self.method = self.request.get_param("demoDependentDropdown")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def process(self, img_two, img_three):
        height, width = img_two.shape[:2]
        img_three_resized = cv2.resize(img_three, (width, height))
        blended_image = cv2.addWeighted(img_two, 0.5, img_three_resized, 0.5, 0)
        difference_image = cv2.absdiff(img_two, img_three_resized)
        return blended_image, difference_image

    def run(self):
        img_two = Image.get_frame(img=self.image_two, redis_db=self.redis_db)
        img_three = Image.get_frame(img=self.image_three, redis_db=self.redis_db)
        res1, res2 = self.process(img_two.value, img_three.value)
        packageModel = self.request.model.dict()
        return packageModel

if "__main__" == __name__:
    Executor(sys.argv[1]).run()
