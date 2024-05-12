<template>
    <div class="section__hedline">
        <h1>{{ credential?.username }}@{{ credential?.app.name }}</h1>
    </div>
    <hr>
    <CredentialForm
        :newCredential="true"
        :credential="credential"
        :apps="apps"
        @saveCredential="saveCredential"
    ></CredentialForm>
</template>
<script lang="ts">
import { defineComponent, onMounted, ref, reactive, computed } from 'vue';
import { CredentialSchema, Credential, AppType } from './components/interfaces.ts';
import { getApps } from './components/appCRUD.ts';
import { getCredential, updateCredential } from './components/credentialCRUD.ts';
import CredentialForm from './views/CredentialForm.vue';

export default defineComponent({
    components: {
        CredentialForm,
    },
    setup() {      
        const credential = ref<Credential>()
        const apps = ref<AppType[]>();
        
        async function getData(): Promise<void>{
            credential.value = await getCredential(credentialId);
            apps.value = await getApps();
        }

        function saveCredential(CredentialSchema: CredentialSchema){
            updateCredential(credentialId, CredentialSchema)
                .then((result: Credential) => {
                    console.log(result);
                    credential.value = result;
                })
                .catch(error=>{
                    console.log(error);
                });
        }

        onMounted(() => {
            getData(); 
        });

        return {
            apps,
            credential,
            saveCredential,
        }
    }
});
</script>