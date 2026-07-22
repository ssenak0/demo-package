from sdks.novavision.src.helper.package import PackageHelper
from novavision.demo_package.models.PackageModel import (
    PackageModel, PackageConfigs, ConfigExecutor, 
    ExecutorOne, ExecutorOneResponse, ExecutorOneOutputs, OutputImageOne,
    ExecutorTwo, ExecutorTwoResponse, ExecutorTwoOutputs, OutputImageTwo, OutputImageThree
)

def build_response_one(context):
    outputImageOne = OutputImageOne(value=context.output_image_one)
    outputs = ExecutorOneOutputs(outputImageOne=outputImageOne)
    response = ExecutorOneResponse(outputs=outputs)
    executorOne = ExecutorOne(value=response)
    configExecutor = ConfigExecutor(value=executorOne)
    packageConfigs = PackageConfigs(executor=configExecutor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    return package.build_model(context)

def build_response_two(context):
    outputImageTwo = OutputImageTwo(value=context.output_image_two)
    outputImageThree = OutputImageThree(value=context.output_image_three)
    outputs = ExecutorTwoOutputs(outputImageTwo=outputImageTwo, outputImageThree=outputImageThree)
    response = ExecutorTwoResponse(outputs=outputs)
    executorTwo = ExecutorTwo(value=response)
    configExecutor = ConfigExecutor(value=executorTwo)
    packageConfigs = PackageConfigs(executor=configExecutor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    return package.build_model(context)
