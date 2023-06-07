<template>
  <div class="home">
    <h1>Bem-vindo ao Sistema de Gerenciamento de Funcionários</h1>
    <p>Aqui você pode controlar todas as informações dos funcionários da sua empresa.</p>
    <div class="features">
      <div class="feature">
        <i class="fas fa-users"></i>
        <h2>Cadastrar Funcionários</h2>
        <p>Registre novos funcionários na plataforma, informando seus dados pessoais e informações de emprego.</p>
      </div>
      <div class="feature">
        <i class="fas fa-list"></i>
        <h2>Lista de Funcionários</h2>
        <p>Visualize todos os funcionários cadastrados, com detalhes como nome, departamento e data de admissão.</p>
      </div>
      <div class="feature">
        <i class="fas fa-edit"></i>
        <h2>Editar Funcionários</h2>
        <p>Atualize as informações dos funcionários, como departamento, cargo e dados pessoais.</p>
      </div>
      <div class="feature">
        <i class="fas fa-trash"></i>
        <h2>Remover Funcionários</h2>
        <p>Remova funcionários do sistema, caso necessário.</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
};
</script>

<style scoped>
.home {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

.features {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin-top: 40px;
}

.feature {
  width: 250px;
  margin: 20px;
  padding: 20px;
  background-color: #f0f0f0;
  border-radius: 8px;
  text-align: center;
}

.feature i {
  font-size: 36px;
  margin-bottom: 10px;
  color: #888;
}

.feature h2 {
  font-size: 20px;
  margin-bottom: 10px;
}

.feature p {
  font-size: 14px;
  color: #777;
}
</style>