import { RegistrationSchema, StatusMessage, ValidationResult } from './interfaces.ts';

export function validateRegistrationSchema(schema: RegistrationSchema): ValidationResult{
    if(schema.email == ""){
        return {
            message: <StatusMessage>{
                type: "error",
                messageClass: "message--error",
                text: "Please enter a email",
            },
            success: <boolean>false
        };
    }

    if(schema.password == "" || schema.passwordConfirm == ""){
        return {
            message: <StatusMessage>{
                type: "error",
                messageClass: "message--error",
                text: "Please enter a password",
            },
            success: <boolean>false
        };
    }
    
    if(schema.password !== schema.passwordConfirm){
        return {
            message: <StatusMessage>{
                type: "error",
                messageClass: "message--error",
                text: "Passwords do not match!",
            },
            success: <boolean>false
        };
    }

    return {
        message: <StatusMessage>{
            type: "success",
            messageClass: "message--success",
            text: "Validation successful!",
        },
        success: <boolean>true
    };
    
}