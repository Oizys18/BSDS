<template>
  <div id="select-one">
    <select v-model="selected" >
      <option disabled value="">하나 선택</option>
      <option>전자기기</option>
      <option>의류</option>
      <option>현금/귀금속</option>
    </select>
    <p>선택함: {{ this.selected }}</p>
  </div>
</template>

<script>
export default {
  name: "selectOne",
  data() {
    return {
      selected: "",
    };
  },
};
</script>

<style scoped>
#select-one .dropdown-toggle{
  border:none;
}
</style>
