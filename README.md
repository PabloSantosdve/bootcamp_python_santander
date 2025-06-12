
# 📁 Git: Do Básico ao Avançado

Guia rápido e sem enrolação dos comandos Git que salvam vidas.

---

## 🟢 BÁSICO

### `git init`
Cria um repositório Git vazio na pasta atual.

### `git clone <url>`
Clona um repositório remoto.

### `git status`
Mostra o que tá rolando no repositório (arquivos modificados, prontos pra commit, etc).

### `git add <arquivo>` ou `git add .`
Adiciona arquivos pro "carrinho" do commit.

### `git commit -m "mensagem"`
Faz o commit das alterações com uma mensagem.

### `git push`
Empurra os commits pro repositório remoto.

### `git pull`
Puxa as mudanças do remoto pra tua branch local.

---

## 🟡 INTERMEDIÁRIO

### `git branch`
Mostra as branches existentes.

### `git checkout -b <nova-branch>`
Cria e já entra numa nova branch.

### `git merge <branch>`
Une outra branch na branch atual.

### `git log`
Mostra o histórico de commits.

### `git stash`
Guarda alterações não commitadas pra você mexer em outra coisa.

### `git stash pop`
Recupera o último stash.

### `git remote -v`
Mostra os repositórios remotos conectados.

---

## 🔴 AVANÇADO / COMPLEXO

### `git rebase <branch>`
Aplica os commits da sua branch em cima de outra. Útil pra deixar o histórico linear.

### `git cherry-pick <hash>`
Aplica um commit específico de outra branch na atual.

### `git reset --hard <hash>`
Volta o repositório pro estado de um commit específico. **Cuidado, isso apaga alterações.**

### `git reflog`
Mostra o histórico de tudo que você fez (até coisas que "sumiram").

### `git revert <hash>`
Cria um commit que desfaz um commit anterior.

### `git clean -fd`
Remove arquivos não rastreados e diretórios.

---

## ☑️ Dicas Finais

- Cria um `.gitignore` decente. Exemplo pra Node:

