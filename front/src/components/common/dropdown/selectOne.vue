<template>
  <!-- <div> -->
    <select
      class="custom-select"
      v-model="this.value"
      v-on:input="updateValue($event.target.value)"
    >
      <option v-for="(item, index) in items" :key="item.id" :value="index">{{
        item
      }}</option>
    </select>
    <!-- <div class="select-box">
      <div class="select-box__current" tabindex="1">
        <div class="select-box__value">
          <input
            class="select-box__input"
            type="radio"
            id="0"
            value="1"
            name="Ben"
            checked="checked"
          />
          <p class="select-box__input-text">Cream</p>
        </div>
        <div class="select-box__value">
          <input
            class="select-box__input"
            type="radio"
            id="1"
            value="2"
            name="Ben"
            checked="checked"
          />
          <p class="select-box__input-text">Cheese</p>
        </div>
        <div class="select-box__value">
          <input
            class="select-box__input"
            type="radio"
            id="2"
            value="3"
            name="Ben"
            checked="checked"
          />
          <p class="select-box__input-text">Milk</p>
        </div>
        <div class="select-box__value">
          <input
            class="select-box__input"
            type="radio"
            id="3"
            value="4"
            name="Ben"
            checked="checked"
          />
          <p class="select-box__input-text">Honey</p>
        </div>
        <div class="select-box__value">
          <input
            class="select-box__input"
            type="radio"
            id="4"
            value="5"
            name="Ben"
            checked="checked"
          />
          <p class="select-box__input-text">Toast</p>
        </div>
        <img
          class="select-box__icon"
          src="http://cdn.onlinewebfonts.com/svg/img_295694.svg"
          alt="Arrow Icon"
          aria-hidden="true"
        />
      </div>
      <ul class="select-box__list">
        <li>
          <label class="select-box__option" for="0" aria-hidden="aria-hidden"
            >Cream</label
          >
        </li>
        <li>
          <label class="select-box__option" for="1" aria-hidden="aria-hidden"
            >Cheese</label
          >
        </li>
        <li>
          <label class="select-box__option" for="2" aria-hidden="aria-hidden"
            >Milk</label
          >
        </li>
        <li>
          <label class="select-box__option" for="3" aria-hidden="aria-hidden"
            >Honey</label
          >
        </li>
        <li>
          <label class="select-box__option" for="4" aria-hidden="aria-hidden"
            >Toast</label
          >
        </li>
      </ul>
    </div> -->
  <!-- </div> -->
</template>

<script>
export default {
  name: "selectOne",
  data() {
    return {
      selected: "",
      value: "선택!",
      items: ["옷", "가방", "신발"],
    };
  },
  // props: ["value", "items"],
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
  padding:0px 10px 0px 10px;
}
.custom-select:focus {
  outline-style: inherit;
}
</style>

// <style lang="scss" scoped>
// .select-box {
//   // position: relative;
//   // display: block;
//   width: 100%;
//   margin: 0 auto;
//   font-family: "Open Sans", "Helvetica Neue", "Segoe UI", "Calibri", "Arial",
//     sans-serif;
//   font-size: 18px;
//   color: #60666d;

//   @media (min-width: 768px) {
//     width: 70%;
//   }

//   @media (min-width: 992px) {
//     width: 50%;
//   }

//   @media (min-width: 1200px) {
//     width: 30%;
//   }

//   &__current {
//     position: relative;
//     box-shadow: 0 15px 30px -10px transparentize(#000, 0.9);
//     cursor: pointer;
//     outline: none;

//     &:focus {
//       & + .select-box__list {
//         opacity: 1;

//         // We have to set "animation-name: none;" to make the list visible (read below how it works)

//         animation-name: none;

//         .select-box__option {
//           cursor: pointer;
//         }
//       }

//       .select-box__icon {
//         transform: translateY(-50%) rotate(180deg);
//       }
//     }
//   }

//   &__icon {
//     position: absolute;
//     top: 50%;
//     right: 15px;
//     transform: translateY(-50%);
//     width: 20px;
//     opacity: 0.3;
//     transition: 0.2s ease;
//   }

//   &__value {
//     display: flex;
//   }

//   &__input {
//     display: none;

//     &:checked + .select-box__input-text {
//       display: block;
//     }
//   }

//   &__input-text {
//     display: none;
//     width: 100%;
//     margin: 0;
//     padding: 15px;
//     background-color: #fff;
//   }

//   &__list {
//     position: absolute;
//     width: 100%;
//     padding: 0;
//     list-style: none;
//     opacity: 0;

//     // We need to use animation with delay.
//     // Otherwise the click event will not have time to run on label, because this element disapears immediately when .select-box__current element loses the focus.
//     // This delay will not be noticed because we set "opacity" to "0".
//     // We also use "animation-fill-mode: forwards" to make the list stay hidden.

//     animation-name: HideList;
//     animation-duration: 0.5s;
//     animation-delay: 0.5s;
//     animation-fill-mode: forwards;
//     animation-timing-function: step-start;
//     box-shadow: 0 15px 30px -10px transparentize(#000, 0.9);
//   }

//   &__option {
//     display: block;
//     padding: 15px;
//     background-color: #fff;

//     &:hover,
//     &:focus {
//       color: #546c84;
//       background-color: #fbfbfb;
//     }
//   }
// }

// @keyframes HideList {
//   from {
//     transform: scaleY(1);
//   }
//   to {
//     transform: scaleY(0);
//   }
// }
// </style>
