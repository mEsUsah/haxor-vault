/**
 * Add shake animation class to an element, and remove it after 1 second.
 * 
 * @param {string} id Element id.
 * @returns {void}
 */
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