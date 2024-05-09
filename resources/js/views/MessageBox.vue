<template>
    <div class="message" :class="statusMessage.messageClass" id="loginAlert">
        <img class="message-icon" 
            :src="assets.warningIcon" 
            alt="warning symbol">
        <p class="message__message">{{statusMessage.text}}</p>
    </div>
</template>

<script lang=ts>
import { PropType, defineComponent, reactive } from 'vue';
import { staticPath } from '../config';

interface StatusMessage {
    type: string,
    messageClass: string,
    text: string,
}

export default defineComponent({
    props: {
        statusMessage: {
            type: Object as PropType<StatusMessage>,
            required: true
        }
    },
    setup(){
        const assets: object = reactive({
            warningIcon: <string>staticPath + 'icons/warning.png'
        });
        return {
            assets
        }
    }

});
</script>