<template>
  <div>
    <navbar />
    <div class="container animated fadeIn fast">
      <div class="created_message">
        <span class="message">
          분실신고 번호
        </span>
        <span>
          {{ this.$store.state.lostname }}
        </span>
      </div>
      <div class="go-index-button">
        <span @click="go('/')">
          <button-huge :text="'첫 페이지로'" />
        </span>
      </div>
    </div>
  </div>
</template>

<script>
import buttonHuge from "@/components/common/button/buttonHuge";
import navbar from "@/views/user/components/navbar";

export default {
  name: "created-user",
  components: {
    buttonHuge,
    navbar,
  },
  methods: {
    go(path) {
      this.$router.push(path);
    },
  },
};
</script>

<style scoped>
.go-index-button {
  position: absolute;
  bottom: 5%;
  right: 5%;
}
.container {
  margin-top: 150px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.created_message {
  margin-top: 150px;
  justify-content: center;
  align-items: center;
  display: flex;
  flex-direction: column;
}
.message {
  margin: 20px;
  font-size: 1.1rem;
  font-weight: bold;
}
</style>
