<template>
  <div class="signup-container">
    <h1>Check</h1>
    <p>성, 이름, 이메일, 생년월일</p>
    <form class="signup-form">
      <div class="form-group">
        <label for="username">LAST NAME</label>
        <input
          type="text"
          id="lastname"
          v-model="localForm.last_name"
          placeholder="Last Name"
        />
        <br />
      </div>
      <div class="form-group">
        <label for="username">FIRST NAME</label>
        <input
          type="text"
          id="firstname"
          v-model="localForm.first_name"
          placeholder="First Name"
        />
        <br />
      </div>
      <div class="form-group">
        <label for="username">EMAIL</label>
        <input
          type="email"
          id="email"
          v-model="localForm.email"
          placeholder="Email"
        />
        <br />
      </div>
      <div class="form-group">
        <label for="username">BIRTH</label>
        <input type="date" id="birth" v-model="localForm.birth" />
        <br />
      </div>
      <div style="display: flex; justify-content: space-between">
        <button class="submit-button-both" @click="goPrevious">Back</button>
        <button class="submit-button-both" @click="goNext">Next</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { reactive } from "vue";
import "@/assets/styles/signup.css";
const props = defineProps(["formData"]);
const emit = defineEmits(["update-data", "next", "previous"]);

const localForm = reactive({
  email: props.formData.email,
  first_name: props.formData.first_name,
  last_name: props.formData.last_name,
  birth: props.formData.birth,
});

const goPrevious = () => {
  emit("previous");
};

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
