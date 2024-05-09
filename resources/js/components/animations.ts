export function animateElementShake(id: string):void {
    const element = document.getElementById(id);
    if(element){
        element.classList.remove("shake");
        element.classList.add("shake");
        setTimeout(() => {
            element.classList.remove("shake");
        }, 1000);
    }
}