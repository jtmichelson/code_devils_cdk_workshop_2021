#!/usr/bin/env python3

from aws_cdk import core

from code_devils_cdk_workshop_2021.code_devils_cdk_workshop_2021_stack import CodeDevilsCdkWorkshop2021Stack


app = core.App()
CodeDevilsCdkWorkshop2021Stack(app, "code-devils-cdk-workshop-2021", env={'region': 'us-west-2'})

app.synth()
