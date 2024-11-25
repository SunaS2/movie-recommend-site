<template>
  <div class="signup-container">
    <h1>닉네임</h1>
    <form class="signup-form">
      <div class="form-group">
        <label for="username">NICKNAME</label>
        <input
          type="text"
          id="nickname"
          v-model="localForm.nickname"
          placeholder="Nickname"
        />
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
  nickname: props.formData.nickname,
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
