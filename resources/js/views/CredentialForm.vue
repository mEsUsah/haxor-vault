<template>
    <form class="form__wrapper">
        <div class="form__field">
            <select name="apptype" v-model="credential.app">
                <option value="" disabled>Select app:</option>
                <option v-for="app in apps" :value="app.id">
                    {{ app.name }}
                </option>
            </select>
        </div>
        <div class="form__field">
            <input v-model="credential.username" type="text" name="username" placeholder="Username" maxlength="100">
        </div>
        <div class="form__field">
            <input v-model="credential.password" type="password" name="password" placeholder="Password" maxlength="100">
        </div>
        <div class="form__buttons">
            <button 
                :disabled="disableSubmit"
                @click="saveCredential"
                type="submit" class="button">Save</button>
            <a href="/dashboard" class="button button--nautral">Back</a>
            <a class="button button--danger"
                v-if="!newCredential"
                @click="destroyCredential"
            >Delete</a>
        </div>
    </form>
</template>

<script lang="ts">
import { defineComponent, PropType, onMounted, ref, reactive, computed, watch } from 'vue';
import { App, CredentialSchema } from '../components/interfaces.ts';
import { validateCredentialSchema } from '../components/validateCredentialSchema.ts';
const csrfToken = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content');

export default defineComponent({
    props: {
        apps: {
            type: Array as PropType<App[]>,
            required: false
        },
        credential: {
            type: Object as PropType<Credential>,
            required: false
        },
        newCredential: {
            type: Boolean,
            required: false,
            default: false
        }
    },
    emits: [
        'saveCredential',
        'destroyCredential'
    ],
    setup(props, ctx) {
        const credential: CredentialSchema = reactive({
            username: "",
            password: "",
            app: "",
            csrfmiddlewaretoken: csrfToken?csrfToken:""
        });

        watch(props, ()=>{
            if(props.credential){
                credential.username = props.credential.username;
                credential.password = props.credential.password;
                credential.app = props.credential.app.id;
            }
            // Get app id from url param, if the app is not set.
            if(props.apps && !credential.app){
                credential.app = getAppFromUrl();
            }
        });
        
        const disableSubmit = computed(()=>{
            return !validateCredentialSchema(credential);
        });

        function saveCredential(event: Event){
            event.preventDefault();
            if(validateCredentialSchema(credential)){
                ctx.emit("saveCredential", credential);
            }
        }

        function destroyCredential(){
            ctx.emit("destroyCredential", credential)
        }

        function getAppFromUrl(): string {
            const queryString = window.location.search;
            const urlParams = new URLSearchParams(queryString);
            const app = urlParams.get('app')
            if(app){
                return app;
            } else {
                return ""
            }
        }

        return {
            credential,
            disableSubmit,
            saveCredential,
            destroyCredential
        }
    }
});
</script>