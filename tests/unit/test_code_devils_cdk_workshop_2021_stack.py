import json
import pytest

from aws_cdk import core
from code_devils_cdk_workshop_2021.code_devils_cdk_workshop_2021_stack import CodeDevilsCdkWorkshop2021Stack


def get_template():
    app = core.App()
    CodeDevilsCdkWorkshop2021Stack(app, "code-devils-cdk-workshop-2021")
    return json.dumps(app.synth().get_stack("code-devils-cdk-workshop-2021").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
