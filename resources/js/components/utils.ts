/**
 * Get master password from local storage in browser.
 * 
 * Redirects to logout page if not found.
 * @returns password
 */
export function getMasterPassword(): string{
    let password = localStorage.getItem("password");
    if (password){
        return password;
    } else {
        window.location.href = "/logout";
        return "";
    }
}

/**
 * Add text to OS clipboard
 * @param text - what to add to clipboard
 */
export function copyToClipboard(text): void{
    navigator.clipboard.writeText(text)
        .then(()=>{
            console.log("copied to clipboard:", text);
        }).catch(error=>{
            console.log(error);
        })
}