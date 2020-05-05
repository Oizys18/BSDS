<template>
  <div>
    <div class="admin-info animated fadeIn fast">
      <span class="admin">
        {{ getUserInfo.parent_department + ' '+  getUserInfo.center_name + getUserInfo.role }}
      </span>
      <div class="admin-detail-info-div">
      <span class="admin-detail-info">
        Tel. {{ getUserInfo.phone_number}}
      </span>
      <span class="admin-detail-info">
        주소. {{ getUserInfo.address[0].address_name }}
      </span>
      </div>
    </div>
    <div id="admin-btn-wrapper" class="animated zoomIn faster">
      <div class="page-link-button">
        <div class="admin-detail-div" @click="go('createFound')">
          <div class="admin-icon">
            <i class="far fa-edit fa-5x icon"></i>
          </div>
          <button-default class="admin-detail-btn" :text="btn1" />
        </div>
        <div class="admin-detail-div" @click="go('createdList')">
          <div class="admin-icon">
            <i class="fas fa-list fa-5x icon"></i>
          </div>
          <button-default class="admin-detail-btn" :text="btn2" />
        </div>
        <div class="admin-detail-div" @click="go('lostList')">
          <div class="admin-icon">
            <i class="fas fa-search fa-5x icon"></i>
          </div>
          <button-default class="admin-detail-btn" :text="btn3" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import buttonDefault from "../../../components/common/button/buttonDefault";
export default {
  name: "adminDetail",
  components: {
    buttonDefault,
  },
  data() {
    return {
      btn1: "습득물 등록",
      btn2: "작성한 글 목록",
      btn3: "분실 신고 목록",
    }
  },
  methods: {
    go(path) {
      this.$router.push({name: path})
    },
  },
  computed: {
    ...mapGetters(['getUserInfo', 'getInfo'])
  },
  // mounted() {
  //   this.$store.dispatch('getUserInfo')
  // }
}
</script>

<style scoped>
  .admin-detail-btn {
    border: none;
  }
  .admin-detail-btn:hover {
    box-shadow: none;
    border: none;
  }
  .admin-detail-btn:active {
    box-shadow: none;
    border: none;
    outline: none;

  }
  .admin-detail-div {
    margin: auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 300px;
    width: 280px;
    box-sizing: border-box;
    border-style: solid;
    border-image: linear-gradient(to right, #0A95FF 80%, #38618C 100%);
    border-image-slice: 1;
    border-image-width: 2px;
  }
  .page-link-button {
    display: grid;
    width: 40%;
    grid-template-rows: repeat(1, 350px);
    grid-template-columns: repeat(3, 300px);
    justify-content: space-around;
    align-items: center;
    margin: 20px;
  }
  #admin-btn-wrapper {
    width: 100%;
    height: 100%;
    margin-top: 20px;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    display: flex;
    flex-wrap: wrap;
  }
  .icon {
    color: #0A95FF;
  }
  .admin-icon {
    display: inline-block;
  }
  .admin-detail-btn {
    position: relative;
    bottom: -20%;
    font-size: 1.1rem;
    font-weight: bold;
    color: #38618C;
  }

  .admin-detail-div:hover {
    box-shadow: 5px 5px 10px 0 #38618C;
    border: 1px solid white;
    outline: none;
  }
  .admin-detail-div:active {
    box-shadow: 5px 5px 10px 0 #0A95FF;
    border: 1px solid white;
    outline: none;
  }
  .admin-info {
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
  }
  .admin {
    margin: 50px 10px 20px 0;
    font-size: 1.5rem;
    font-weight: bold;
  }
  .admin-detail-info-div {
    width: 30%;
    text-align: initial;
    padding-left: 50px;
  }
  .admin-detail-info {
    display: block;
    font-size: 1rem;
    margin: 3px;
  }

</style>