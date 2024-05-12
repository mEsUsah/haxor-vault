const s3path: string = "https://devsearch-bucket.eu-central-1.linodeobjects.com/vault.haxor.no/static/";
export const staticPath:string = process.env.NODE_ENV === "production" ? s3path : "/static/";
export const api_host = "http://127.0.0.1:8000";
export const api_apps = "/api/v1/apps";
export const api_apptypes = "/api/v1/apptypes";
export const api_credentials = "/api/v1/credentials";

console.log('staticPath:', staticPath);