export interface StatusMessage {
    type: string,
    messageClass: string,
    text: string,
}

export interface AuthenticationData {
    username: string,
    password: string,
    csrfmiddlewaretoken: string
}

export interface AppSchema{
    name: string,
    apptype: string,
    csrfmiddlewaretoken: string,
}
export interface CredentialSchema{
    username: string,
    password: string,
    app: string,
    csrfmiddlewaretoken: string,
}

export interface Credential{
    app: App,
    id: string,
    password: string,
    username: string,
}

export interface AppType{
    id: string,
    name: string,
}

export interface App {
    id: string,
    name: string,
    apptype: AppType,
    credentials: Array<Credential>,
    user: number
};

