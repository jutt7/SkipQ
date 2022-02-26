import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as cdk from "@aws-cdk/core";
///import * as lambda_ from '@aws-cdk/aws-lambda';
import { aws_lambda as lambda_ } from 'aws-cdk-lib';

// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class AwaisSprint4StackStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here

    const HWLambda = new lambda_.Function(this, 'MyLambdaFunction', {
      runtime: lambda_.Runtime.NODEJS_12_X,
       handler: 'WebHealth_lambda.lambdaHandler',
      code: lambda_.Code.fromAsset('resources'),
});

    // example resource
    // const queue = new sqs.Queue(this, 'AwaisSprint4StackQueue', {
    //   visibilityTimeout: cdk.Duration.seconds(300)
    // });
  }
}
