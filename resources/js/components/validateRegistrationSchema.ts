import { RegistrationSchema, StatusMessage, ValidationResult } from './interfaces.ts';

/**
 * Validates the registration schema.
 * 
 * @param {RegistrationSchema} schema  Registration schema.
 * @returns {ValidationResult} Object containing a message and a success boolean.
 */
export function validateRegistrationSchema(schema: RegistrationSchema): ValidationResult{
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    if (!schema.email.match(emailRegex) || schema.email.trim() == "") {
        return {
            message: <StatusMessage>{
                type: "error",
                messageClass: "message--error",
                text: "Please enter a valid email address",
            },
            success: <boolean>false
        };
    }

    if(schema.password.trim() == "" || schema.passwordConfirm.trim() == ""){
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