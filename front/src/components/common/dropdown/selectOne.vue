<template>
  <select
    class="custom-select"
    v-model="selectOne"
    v-on:input="updateValue($event.target.value)"
  >
    <option value="">{{ this.default }}</option>
    <option v-for="(item, index) in items" :key="item.id" :value="index">{{
      item
    }}</option>
  </select>
</template>

<script>
export default {
  name: "selectOne",
  data() {
    return {
      selectOne: "",
    };
  },
  props: {
    default: {
      type: String,
      default: "선택해주세요",
    },
    items: {
      type: Object,
      default: function() {
        return {};
      },
    },
  },
  methods: {
    updateValue: function(value) {
      this.$emit("input", value);
    },
  },
};
</script>

<style scoped>
.custom-select {
  width: 200px;
  border: 1px solid black;
  border-radius: 15px;
  padding: 0px 10px 0px 10px;
}
.custom-select:focus {
  outline-style: inherit;
}
</style>
