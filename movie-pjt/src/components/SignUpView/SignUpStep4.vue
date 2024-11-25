<template>
    <div class="signup-container">
        <h1>학습 레벨</h1>
        <p>학습 레벨을 선택하지 않으면 자동으로 초급 단계가 됩니다.</p>
        <form class="signup-form" @submit.prevent="submit">
            <div class="form-group">
                <label for="studylevel">STUDY LEVEL</label>
                <!-- 토글 버튼 -->
                <div class="dropdown-container">
                    <button type="button" class="dropdown-button" @click="toggleDropdown">
                        {{ localForm.studylevel || 'Select your level' }}
                    </button>
                    <!-- 드롭다운 -->
                    <div v-if="isDropdownOpen" class="dropdown-options">
                        <button
                            v-for="level in levels"
                            :key="level"
                            class="dropdown-option"
                            @click="selectLevel(level)"
                        >
                            {{ level }}
                        </button>
                    </div>
                </div>
                <br>
            </div>
            <div style="display: flex; justify-content: space-between;">
                <button type="button" class="submit-button-both" @click="goPrevious">Back</button>
                <button type="submit" class="submit-button-both">Submit</button>
            </div>
        </form>
    </div>
</template>



<script setup>
import { ref, reactive } from 'vue';
import "@/assets/styles/signup.css";

const props = defineProps(['formData']);
const emit = defineEmits(['submit', 'previous']);

// 학습 레벨 리스트
const levels = ref(['A1', 'A2', 'B1', 'B2', 'C1', 'C2']);

// 폼 데이터
const localForm = reactive({
    studylevel: props.formData.study_level
});

// 드롭다운 상태 관리
const isDropdownOpen = ref(false);

// 드롭다운 열기/닫기
const toggleDropdown = () => {
    isDropdownOpen.value = !isDropdownOpen.value;
};

// 레벨 선택
const selectLevel = (level) => {
    localForm.studylevel = level;
    isDropdownOpen.value = false; // 선택 후 드롭다운 닫기
};

// 이전 단계로 이동
const goPrevious = () => {
    emit('previous');
};

// 데이터 제출
const submit = () => {
    if (!localForm.studylevel) {
        alert("학습 레벨을 선택해주세요.");
        return;
    }
    props.formData.study_level = localForm.studylevel;
    emit('submit', props.formData); // 최종 데이터 전달
};
</script>



<style scoped>
/* 드롭다운 컨테이너 */
.dropdown-container {
    position: relative;
    width: 100%;
}

/* 드롭다운 버튼 */
.dropdown-button {
    width: 100%;
    padding: 0.8rem;
    border-radius: 2rem;
    background: #333;
    color: #fff;
    border: none;
    cursor: pointer;
    font-size: 1rem;
    text-align: center;
}

/* 드롭다운 옵션 리스트 */
.dropdown-options {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: #444;
    border-radius: 2rem;
    margin-top: 0.5rem;
    padding: 0.5rem;
    z-index: 10;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

/* 옵션 버튼 스타일 */
.dropdown-option {
    padding: 0.8rem;
    border-radius: 2rem;
    background: #555;
    color: #fff;
    border: none;
    cursor: pointer;
    font-size: 1rem;
    text-align: center;
}

/* 옵션 버튼 호버 스타일 */
.dropdown-option:hover {
    background: #666;
}

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