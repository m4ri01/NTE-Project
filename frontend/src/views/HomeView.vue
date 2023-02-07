<script lang="ts">
import axios from "axios";
import Swal from "sweetalert2";
import ItemSearch from "../components/ItemSearch.vue";

export default {
  components: {
    ItemSearch,
  },
  data() {
    return {
      form: {
        dataType: "",
        query: "",
      },
      items: {
        name: "",
        NDInternet: "",
        SNONT: "",
        alamat: "",
        longitude: "",
        latitude: "",
        ODP: "",
        status: "",
        firstONT:"",
        lastONT:"",
        statusONT:"",
      },
    };
  },
  methods: {
    cari() {
      axios({
        method: "GET",
        url: "http://localhost:5000/ont/",
        params:{
          name: this.form.query,          
          dataType: this.form.dataType,
        },
        headers: {},
        data: {},
      })
        .then((response) => {
          // console.log(response.data);
          // Swal.fire("Success!", "Berhasil mendapatkan data", "success");
          this.items = response.data;
        })
        .catch((error) => {
          Swal.fire(
            "Failed!",
            error.response.data.error
              ? `${error.response.data.error} (${error.response.status})`
              : `Request gagal tanpa error message (${error.response.status})`,
            "error"
          );
          console.log(error);
        });
    },
  },
};
</script>

<template>
  <main>
    <div class="jumbotron jumbotron-fluid header">
      <img
        class="header-img"
        style="object-fit: cover; overflow: hidden"
        src="../assets/header.png"
        alt="Header"
      />
    </div>
    <div class="container my-3">
      <div class="d-flex align-items-center justify-content-center">
        <h3>
          <strong>Search NTE</strong>
        </h3>
      </div>
      <div class="d-flex justify-content-center align-items-center">
        <div class="justify-content-end m-2">
          <div class="input-group">
            <select v-model="form.dataType" class="form-control">
              <option value="" selected>Search Mode</option>
              <option value="SNONT">SN ONT</option>
              <option value="NDInternet">ND Internet</option>
            </select>
          </div>
        </div>
        <div class="justify-content-start m-2">
          <div class="input-group">
            <input
              v-model="form.query"
              type="text"
              class="form-control"
              aria-label="Amount (to the nearest dollar)"
            />
            <div class="input-group-append">
              <a @click="cari()" href="#">
                <img
                  class="input-group-text"
                  src="../assets/magnifying-glass-solid.svg"
                  alt="search"
                  width="50"
                />
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container-fluid bg-primary mb-3">
      <!-- <div v-for="item in items" v-bind:key="item.id"> -->
      <ItemSearch v-if="items.name" :item="items" />
      <div v-else>
        <h2></h2>
      </div>
      <!-- </div> -->
    </div>
    <div class="row mb-4 blank-space"><h1></h1></div>
  </main>
</template>

<style scoped>
.header {
  background-color: antiquewhite;
}

.header-img {
  width: 100%;
  height: 500px;
}
.blank-space {
  min-height: 100px;
}
</style>
