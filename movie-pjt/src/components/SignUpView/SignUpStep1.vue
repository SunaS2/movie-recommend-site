<template>
    <div class="signup-container">
        <h1>Check</h1>
        <p>username, password, ID</p>
        <form class="signup-form">
            <div class="form-group">
              <label for="username">USERNAME</label>
              <input type="text" id="username" v-model="localForm.username" placeholder="ID">
              <br>
            </div>
            <div class="form-group">
              <label for="username">PASSWORD</label>
              <input type="password" id="password1" v-model="localForm.password1" placeholder="Password">
              <br>
            </div>
            <div class="form-group">
              <label for="username">CONFIRM PASSWORD</label>
              <input type="password" id="password2" v-model="localForm.password2" placeholder="Confirm Password">
              <br>
            </div>
            <button class="submit-button" @click="goNext">Next</button>
        </form>
    </div>
</template>

<script setup>
import { reactive, toRefs } from "vue";
import "@/assets/styles/signup.css";

// 부모 컴포넌트에서 전달된 데이터
const props = defineProps(["formData"]);
const emit = defineEmits(["update-data", "next"]);

// 로컬 상태로 데이터 복사
const localForm = reactive({
  username: props.formData.username,
  password1: props.formData.password1,
  password2: props.formData.password2,
});

// 다음 단계로 이동
const goNext = () => {
  emit("update-data", localForm); // 부모 컴포넌트로 데이터 전달
  emit("next"); // 다음 단계로 이동 이벤트
};
</script>

<style scoped>
p {
    margin-bottom: 1.5rem;
    color: rgba(84, 83, 83, 0.8);
}

input[type="text"],
input[type="password"],
input[type="email"],
input[type="date"] {
    width: 100%;
    padding: 0.8rem;
    border: none;
    background: #333;
    color: #fff;
    font-size: 1rem;
    border-radius: 2rem;
    /* 둥근 모서리 */
}

label {
    color: rgba(255, 255, 255, 0.6);
    margin: 0.3rem;
}
</style>
