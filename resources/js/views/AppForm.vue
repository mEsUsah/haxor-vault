<template>
    <div class="form__wrapper">
        <div class="form__field">
            <select name="apptype" v-model="app.apptype">
                <option value="" disabled>Select type:</option>
                <option v-for="appType in appTypes" :value="appType.id">
                    {{ appType.name }}
                </option>
            </select>
        </div>
        <div class="form__field">
            <input v-model="app.name" type="text" name="name" placeholder="Name">
        </div>
        <div class="form__buttons">
            <button 
                :disabled="disableSubmit"
                @click="saveApp"
                type="submit" class="button">Save</button>
            <a href="/dashboard" class="button button--nautral">Cancel</a>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent, PropType, onMounted, ref, reactive, computed } from 'vue';
import { AppType, AppSchema } from '../components/interfaces.ts';
export default defineComponent({
    props: {
        appTypes: {
            type: Array as PropType<AppType[]>,
            required: false
        }
    },
    emits: [
        'saveApp'
    ],
    setup(props, ctx) {
        const app: AppSchema = reactive({
            name: "",
            apptype: "",
            csrfmiddlewaretoken: csrfToken
        });
        
        const disableSubmit = computed(()=>{
            return app.name == "" || app.apptype == "";
        })

        function saveApp(){
            if(!disableSubmit.value){
                ctx.emit("saveApp", app);
            }
        }

        return {
            app,
            disableSubmit,
            saveApp
        }
    }
});
</script>