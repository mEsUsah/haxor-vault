import { AppSchema } from '../components/interfaces.ts';

/**
 * Validates the app schema.
 * 
 * @param {AppSchema} app App schema.
 * @returns {Boolean}
 */
export function validateAppSchema(app: AppSchema): Boolean {
    if (app.name.trim() === "" || app.name.length > 100) {
        return false;
    }
    if(app.apptype.trim() === "") {
        return false;
    }
    return true;

}