<script lang="ts">
import axios from "axios";
import Swal from "sweetalert2";
export default {
  data() {
    return {
      form: {
        name: "",
        nd_inet: "",
        sn_ont: "",
        alamat: "",
        longitude: "",
        latitude: "",
        odp: "",
        statusONT: ""
      },
    };
  },
  methods: {
    submitForm() {
      console.log(this.form);
      axios({
        method: "POST",
        url: "http://localhost:5000/ont/",
        headers: {},
        data: {
          name: this.form.name,
          NDInternet: this.form.nd_inet,
          SNONT: this.form.sn_ont,
          alamat: this.form.alamat,
          longitude: this.form.longitude,
          latitude: this.form.latitude,
          ODP: this.form.odp,
          statusONT:this.form.statusONT,
        },
      })
        .then((response) => {
          Swal.fire("Success!", "Berhasil menambahkan data", "success");
        })
        .catch((error) => {
          console.log(error.response.data);
          Swal.fire(
            "Failed!",
            error.response.data.error
              ? `${error.response.data.error}`
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
  <div class="input-page">
    <div class="container shadow rounded p-4">
      <div class="row g-3 align-items center mt-2">
        <h3 class="text-center">
          <strong>Input NTE</strong>
        </h3>
      </div>
      <div class="row g-3 align-items-center mt-2">
        <div class="col-2"></div>
        <div class="col-1">
          <label for="name" class="col-form-label">Name</label>
        </div>
        <div class="col-6">
          <input
            v-model="form.name"
            type="text"
            id="name"
            class="form-control"
          />
        </div>
      </div>
      <div class="row g-3 align-items-center mt-2">
        <div class="col-2"></div>
        <div class="col-1">
          <label for="nd_inet" class="col-form-label">ND Inet</label>
        </div>
        <div class="col-6">
          <input
            v-model="form.nd_inet"
            type="text"
            id="nd_inet"
            class="form-control"
          />
        </div>
      </div>
      <div class="row g-3 align-items-center mt-2">
        <div class="col-2"></div>
        <div class="col-1">
          <label for="sn_ont" class="col-form-label">SN ONT</label>
        </div>
        <div class="col-6">
          <input
            v-model="form.sn_ont"
            type="text"
            id="sn_ont"
            class="form-control"
          />
        </div>
      </div>
      <div class="row g-3 align-items-center mt-2">
        <div class="col-2"></div>
        <div class="col-1">
          <label for="alamat" class="col-form-label">Alamat</label>
        </div>
        <div class="col-6">
          <input
            v-model="form.alamat"
            type="text"
            id="alamat"
            class="form-control"
          />
        </div>
      </div>
      <div class="row g-3 align-items-center mt-2">
        <div class="col-2"></div>
        <div class="col-1">
          <label for="longitude" class="col-form-label">Longitude</label>
        </div>
        <div class="col-6">
          <input
            v-model="form.longitude"
            type="number"
            id="longitude"
            class="form-control"
            placeholder="Contoh: 113.xxxx"
          />
        </div>
      </div>
      <div class="row g-3 align-items-center mt-2">
        <div class="col-2"></div>
        <div class="col-1">
          <label for="latitude" class="col-form-label">Latitude</label>
        </div>
        <div class="col-6">
          <input
            v-model="form.latitude"
            type="number"
            id="latitude"
            class="form-control"
            placeholder="Contoh: -3.xxx"
          />
        </div>
      </div>
      <div class="row g-3 align-items-center mt-2">
        <div class="col-2"></div>
        <div class="col-1">
          <label for="odp" class="col-form-label">ODP</label>
        </div>
        <div class="col-6">
          <input v-model="form.odp" type="text" id="odp" class="form-control" />
        </div>
      </div>
      <div class="row g-3 align-items-center mt-2">
        <div class="col-2"></div>
        <div class="col-1">
          <label for="odp" class="col-form-label">Status</label>
        </div>
        <div class="col-6">
          <select v-model="form.statusONT">
            <option disabled value="">Please select one</option>
            <option value=1>Online</option>
            <option value=0>Offline</option>
          </select>
        </div>
      </div>
      <div class="row g-3 align-items-center mt-2">
        <div class="col-3"></div>
        <div class="col-6 text-center">
          <button @click="submitForm()" class="btn btn-primary">Submit</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .input-page {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
