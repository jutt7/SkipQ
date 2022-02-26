// export async function lambda_handler(event:any) {
//     return {
//         message: 'hello'+event
//     };
// };

export const lambdaHandler = (event: any) => {
    "Hello " + event["firstname"] + event["lastname"]
}