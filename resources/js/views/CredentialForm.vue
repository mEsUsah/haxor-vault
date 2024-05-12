<template>
    <div class="form__wrapper">
        <div class="form__field">
            <select name="apptype" v-model="credential.app">
                <option value="" disabled>Select app:</option>
                <option v-for="app in apps" :value="app.id">
                    {{ app.name }}
                </option>
            </select>
        </div>
        <div class="form__field">
            <input v-model="credential.username" type="text" name="name" placeholder="Name">
        </div>
        <div class="form__field">
            <input v-model="credential.password" type="password" name="password" placeholder="Password">
        </div>
        <div class="form__buttons">
            <button 
                :disabled="disableSubmit"
                @click="saveCredential"
                type="submit" class="button">Save</button>
            <a href="/dashboard" class="button button--nautral">Cancel</a>
            <button class="button button--danger"
                v-if="!newCredential"
                @click="destroyCredential"
            >Delete</button>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent, PropType, onMounted, ref, reactive, computed, watch } from 'vue';
import { App, CredentialSchema } from '../components/interfaces.ts';
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
            csrfmiddlewaretoken: csrfToken
        });

        watch(props, ()=>{
            if(props.credential){
                credential.username = props.credential.username;
                credential.password = props.credential.password;
                credential.app = props.credential.app;
            }
        })
        
        const disableSubmit = computed(()=>{
            return credential.username == "" 
                || credential.password == ""
                || credential.app == "";
        })

        function saveCredential(){
            if(!disableSubmit.value){
                ctx.emit("saveCredential", credential);
            }
        }

        function destroyCredential(){
            ctx.emit("destroyCredential", credential)
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