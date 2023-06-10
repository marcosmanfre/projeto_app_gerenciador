<template>
  <div class="container-fluid">    
    <div class="dashboard card-body">
      <div class="card card-nav-tabs">
        <div class="card-header card-header-warning">Cadastro de Pessoas</div>

        <div class="card-body col-md">
<div class="card-body">
<button type="button"
class="btn btn-primary m-2 fload-end"
data-bs-toggle="modal"
data-bs-target="#exampleModal"
@click="addClick()">
 Adicionar Funcionário
</button>
</div>
    

          <div class="col-md-3">
            <div class="input-group mb-3">
              <input
                type="text"
                class="form-control"
                placeholder="Digite o nome para buscar"
                v-model="searchTerm" @keydown.enter="searchClick"
              />
              <div class="input-group-append">
                <button
                  class="btn btn-secondary"
                  type="button"
                  @click="searchClick"
                >
                  Buscar
                </button>
              </div>
            </div>
          </div>
        </div>
        
         <div>
        <table class="table table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>Registro</th>
              <th :style="{ textAlign: 'left' }">Nome</th>
              <th>Departamento</th>
              <th>Cargo</th>
              <th>Data de Cadastro</th>


              <th>Opções</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="emp in employees">
                <td>{{ emp.EmployeeId }}</td>
                <td>{{ emp.Register }}</td>
                <td :style="{ textAlign: 'left' }">{{ emp.EmployeeName }}</td>
                <td>{{ emp.Department }}</td>
                <td>{{ emp.Role }}</td>
                <td>{{ emp.DateOfJoining }}</td>



              <td>
              
                <button
                  type="button"
                  class="btn btn-light mr-1"
                  data-bs-toggle="modal"
                  data-bs-target="#exampleModal"
                  @click="editClick(emp)"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    fill="currentColor"
                    class="bi bi-pencil-square"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"
                    />
                    <path
                      fill-rule="evenodd"
                      d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"
                    />
                  </svg>
                </button>
                <button
                  type="button"
                  @click="deleteClick(emp.EmployeeId)"
                  class="btn btn-light mr-1"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    fill="currentColor"
                    class="bi bi-trash-fill"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"
                    />
                  </svg>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
        <div
          class="modal fade"
          id="exampleModal"
          tabindex="-1"
          aria-labelledby="exampleModalLabel"
          aria-hidden="true"
        >
          <div class="modal-dialog modal-xl modal-dialog-centered">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">
                  {{ modalTitle }}
                </h5>
                <button
                  type="button"
                  class="btn-close"
                  data-bs-dismiss="modal"
                  aria-label="Close"
                ></button>
  
              <form class="row g-3">
              <div class="modal-body">                
                <div class="row">
       
                    <div class="input-group mb-3">
                      <span class="input-group-text">Registro</span>
                      <input
                        type="number"
                        class="form-control"
                        v-model="Register"
                        required
                        id="needs-validation" 
                      />
                    </div>
                  </div>
                  <div class="col-md-6">
                    <div class="input-group mb-3">
                      <span class="input-group-text">Nome</span>
                      <input type="text" class="form-control" v-model="EmployeeName" required
                        id="needs-validation" />
                    </div>
                  </div>
                  <div class="col-md-3">
                    <div class="input-group mb-3">
                      <span class="input-group-text">Departamento</span>
                      <select class="form-select" v-model="Department">
                        <option value="RH">RH</option>
                        <option value="TI">TI</option>
                        <option value="Vendas">Vendas</option>
                        <option value="Financeiro">Financeiro</option>
                        <option value="Produção">Produção</option>
                        <option value="Marketing">Marketing</option>
                        <option value="Logística">Logística</option>                  
                         </select>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-md-3">
                    <div class="input-group mb-3">
                      <span class="input-group-text">Cargo</span>
                      <select class="form-select" v-model="Role">
                        <option value="Gerente">Gerente</option>
                        <option value="Analista">Analista</option>
                        <option value="Desenvolvedor">Desenvolvedor</option>
                        <option value="Coordenador">Coordenador</option>
                        <option value="Assistente">Assistente</option>
                        <option value="Estagiário">Estagiário</option>
                      </select>
                    </div>
                  </div>

                  <div class="col-md-6">
                    <div class="input-group mb-3">
                      <span class="input-group-text">Data de Cadastro</span>
                      <input
                        type="date"
                        class="form-control"
                        v-model="DateOfJoining"
                      />
                    </div>
              
                
                  </div>
                </div>

              
</form>
              <div class="modal-footer">
                <button
                  type="button"
                  @click="createClick()"
                  v-if="EmployeeId == 0"
                  class="btn btn-primary"
                >
                  Inserir
                </button>
                <button
                  type="button"
                  @click="updateClick()"
                  v-if="EmployeeId != 0"
                  class="btn btn-primary"
                >
                  Atualizar
                </button>
              </div>
            </div>
            
          </div>
          
        </div>
        </div>
        
        
      </div>
      
    </div>
    
      </div>
     
    
  </div>
  
</template>

<script>
const variables = {
  API_URL: "http://127.0.0.1:8000/",
};

import axios from "axios";

export default {
  name: "Cadastro",
  data() {
    return {
      employees: [],
      modalTitle: "",
      EmployeeId: 0,      
      Register: "",
      EmployeeName: "",
      Department: "",
      Role: "",
      DateOfJoining: "",
      searchTerm: "",
    };
  },

  methods: {
    refreshData() {
      axios.get(variables.API_URL + "employee").then((response) => {
        this.employees = response.data;
      });
    },
    addClick() {
      this.modalTitle = "Adicionar Pessoa";
      this.EmployeeId = 0;
      this.Register = "";
      this.EmployeeName = "";
      this.Department = "";
      this.Role = "";
      this.DateOfJoining = "";

    },
  
    editClick(emp) {
      this.modalTitle = "Editar Pessoa";
      this.EmployeeId = emp.EmployeeId;
      this.Register = emp.Register;
      this.EmployeeName = emp.EmployeeName;
      this.Department = emp.Department;
      this.Role = emp.Role;
      this.DateOfJoining = emp.DateOfJoining;
     
    },
    createClick() {
      
      let errors = {};

      if (!this.Register) errors.Register = "O registro é obrigatório.";
      if (!this.EmployeeName) errors.EmployeeName = "O nome é obrigatório.";

      if (Object.keys(errors).length > 0) {
    alert("Por favor, corrija os seguintes erros:\n\n" + JSON.stringify(errors, null, 2));
    return;
  }
      axios
        .post(variables.API_URL + "employee", {
          Register: this.Register,
          EmployeeName: this.EmployeeName,
          Department: this.Department,
          Role: this.Role,
          DateOfJoining: this.DateOfJoining,
      
        })
        .then((response) => {
          this.refreshData();
          

          alert(response.data);
        });
        
    },
    updateClick() {
      axios
        .put(variables.API_URL + "employee", {
            EmployeeId: this.EmployeeId,
            Register: this.Register,
            EmployeeName: this.EmployeeName,
            Department: this.Department,
            Role: this.Role,
            DateOfJoining: this.DateOfJoining,
          
        })
        .then((response) => {
          this.refreshData();
          alert(response.data, "pessoa editado com sucesso");
        })
     
    },
    searchClick() {
      axios.get(variables.API_URL + "employee").then((response) => {
        this.employees = response.data.filter((emp) =>
          emp.EmployeeName.toLowerCase().includes(this.searchTerm.toLowerCase())
        );
      });
    },
    deleteClick(id) {
      if (!confirm("Tem certeza que deseja excluir?")) {
        return;
      }
      axios.delete(variables.API_URL + "employee/" + id).then((response) => {
        this.refreshData();
        alert(response.data);
      });
    },
  },

  mounted: function () {
    this.refreshData();
  },
};
</script>
