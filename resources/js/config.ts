const s3path: string = "https://devsearch-bucket.eu-central-1.linodeobjects.com/vault.haxor.no/static/";
export const staticPath:string = process.env.NODE_ENV === "production" ? s3path : "/static/";
console.log('staticPath:', staticPath);