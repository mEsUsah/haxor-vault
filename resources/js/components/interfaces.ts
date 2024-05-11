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

export interface Credential{
    app: string,
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
    credentials: Array<Credential|null>,
    user: number
};