<template>
  <div class="main-container">
    <nav class="navbar navbar-expand-lg bg-body-tertiary rounded-custom" v-if="!isPopup">
      <div class="container-fluid">
        <RouterLink :to="{name:'profile', params:{username:store.logedinUsername}}" 
                    class="navbar-brand styled-hello" 
                    v-if="store.isLogin && store.logedinUsername">
          안녕하세요! {{ store.logedinUsername }} 님!
        </RouterLink>
        <RouterLink :to="{name:'movies'}" 
                    class="navbar-brand mx-auto styled-movie">
          MoviENg
        </RouterLink>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
            <li class="nav-item mx-2">
              <RouterLink :to="{name:'login'}" v-if="!store.isLogin" class="nav-link active styled-button" aria-current="page">Log in</RouterLink>
            </li>
            <li class="nav-item mx-2">
              <RouterLink :to="{name:'signup'}" v-if="!store.isLogin" class="nav-link active styled-button" aria-current="page">Sign Up</RouterLink>
            </li>
            <li class="nav-item mx-2" v-if="store.isLogin && store.logedinUsername">
              <RouterLink :to="{name:'wishmovies', params:{username:store.logedinUsername}}" class="styled-button">Wish Movie</RouterLink>
            </li>
            <li class="nav-item mx-2" v-if="store.isLogin && store.logedinUsername">
              <RouterLink :to="{name:'mynotelist', params:{username:store.logedinUsername}}" class="styled-button">Voca Note</RouterLink>
            </li>
            <li class="nav-item mx-2" v-if="store.isLogin">
              <button @click="store.logOut" class="styled-button logout">Log out</button>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <RouterView/>
    <chatBot v-if="!route.meta.isPopup && store.isLogin"/>
    <footer>
      <div>
        <p>ⓒ 2024. </p>
      </div>
    </footer>
  </div>
  </template>
    
  <script setup>
    import { useMovieStore } from '@/stores/movie';
    import chatBot from '@/components/chatBot.vue';
    import { computed } from 'vue';
    import { useRoute } from 'vue-router';
  
  const store = useMovieStore()
  
  const route = useRoute();
  
  // 팝업 여부를 라우트의 meta 정보로 확인
  const isPopup = computed(()=>route.meta.isPopup || false)
  </script>
    
  <style scoped>
  /* 버튼 스타일 */
  .styled-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 14px 20px; /* 세로를 더 통통하게 */
  font-size: 14px;
  font-weight: 750;
  color: #434040;
  background: rgba(255, 255, 255, 0.15); /* 살짝 투명한 배경 */
  backdrop-filter: blur(8px); /* 유리효과 */
  border-radius: 20px; /* 둥근 모서리 */
  border: 1px solid rgba(90, 90, 90, 0.226); /* 연한 테두리 */
  cursor: pointer;
  gap: 8px; /* 아이콘과 텍스트 간격 */
  transition: background 0.3s ease, transform 0.2s ease; /* 부드러운 효과 */
  text-decoration: none;
  box-shadow:0 4px 10px rgba(0, 0, 0, 0.1);
  }

.styled-button:hover{
  background: rgba(145, 145, 145, 0.25); /* 조금 더 진한 빨간 배경 */
  transform: translateY(-1px); /* 살짝 올라가는 효과 */
  color: #292828; /* 텍스트를 더 진하게 */
}

  /* Log-out 버튼 스타일 */
.styled-button.logout {
  background: rgba(255, 102, 102, 0.15); /* 연한 빨간 계열 배경 */
  color: #ff6666; /* 텍스트를 빨간 계열로 */
  border: 1px solid rgba(255, 102, 102, 0.4); /* 연한 빨간 테두리 */
  transition: background 0.3s ease, transform 0.2s ease; /* 부드러운 전환 */
}

/* Log-out 버튼 호버 효과 */
.styled-button.logout:hover {
  background: rgba(255, 102, 102, 0.25); /* 조금 더 진한 빨간 배경 */
  transform: translateY(-1px); /* 살짝 올라가는 효과 */
  color: #ff4d4d; /* 텍스트를 더 진하게 */
}
</style>