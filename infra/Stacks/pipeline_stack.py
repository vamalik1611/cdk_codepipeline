from aws_cdk import (
    aws_s3 as s3,
    aws_s3_assets as s3_assets,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as codepipeline_actions,    
    core
)

class PipelineStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

