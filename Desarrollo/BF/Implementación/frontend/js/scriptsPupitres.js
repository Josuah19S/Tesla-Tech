function allowDrop(ev) {
    ev.preventDefault();
  }
  
  function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
  }
  
  function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data));
    updateUserView();
  }
  
  function updateUserView() {
    const adminViewRows = document.querySelectorAll('#admin-view .row');
    const userViewRows = document.querySelectorAll('#user-view .row');
  
    adminViewRows.forEach((row, rowIndex) => {
      const mesas = row.querySelectorAll('.mesa');
      const userRow = userViewRows[rowIndex];
      userRow.innerHTML = '';
      mesas.forEach(mesa => {
        const mesaClone = mesa.cloneNode(true);
        mesaClone.setAttribute('draggable', false);
        userRow.appendChild(mesaClone);
      });
    });
  }
  
  document.addEventListener('DOMContentLoaded', () => {
    const mesas = document.querySelectorAll('.mesa');
    mesas.forEach((mesa, index) => {
      mesa.id = `mesa-${index}`;
    });
  });





// function allowDrop(ev) {
//     ev.preventDefault();
//   }
  
//   function drag(ev) {
//     ev.dataTransfer.setData("text", ev.target.id);
//   }
  
//   function drop(ev) {
//     ev.preventDefault();
//     const data = ev.dataTransfer.getData("text");
//     const draggedElement = document.getElementById(data);
//     const dropTarget = ev.target;
  
//     // Verifica que el objetivo de la caída no sea descendiente del elemento arrastrado
//     if (draggedElement && !draggedElement.contains(dropTarget) && (dropTarget.classList.contains('droppable') || dropTarget.classList.contains('mesa'))) {
//       dropTarget.appendChild(draggedElement);
//       saveState();
//       updateUserView();
//     }
//   }
  
//   function saveState() {
//     const adminViewRows = document.querySelectorAll('#admin-view .row');
//     const state = [];
  
//     adminViewRows.forEach(row => {
//       const mesas = [];
//       row.querySelectorAll('.mesa').forEach(mesa => {
//         mesas.push({
//           class: mesa.className,
//           content: mesa.textContent.trim()
//         });
//       });
//       state.push(mesas);
//     });
  
//     localStorage.setItem('mesasState', JSON.stringify(state));
//   }
  
//   function loadState() {
//     const state = JSON.parse(localStorage.getItem('mesasState'));
  
//     if (state) {
//       const adminViewRows = document.querySelectorAll('#admin-view .row');
//       adminViewRows.forEach((row, rowIndex) => {
//         row.innerHTML = ''; // Limpia la fila antes de añadir las mesas
  
//         if (state[rowIndex]) { // Verifica que la fila exista en el estado guardado
//           state[rowIndex].forEach((mesaState, mesaIndex) => {
//             const mesa = document.createElement('div');
//             mesa.className = mesaState.class;
//             mesa.textContent = mesaState.content;
//             mesa.setAttribute('draggable', true);
//             mesa.setAttribute('ondragstart', 'drag(event)');
//             mesa.id = `mesa-${rowIndex}-${mesaIndex}`;  // Asegura un id único para cada mesa
//             row.appendChild(mesa);
//           });
//         }
//       });
  
//       updateUserView();
//     }
//   }
  
//   function updateUserView() {
//     const state = JSON.parse(localStorage.getItem('mesasState'));
//     if (state) {
//       const userViewRows = document.querySelectorAll('#user-view .row');
//       userViewRows.forEach((row, rowIndex) => {
//         row.innerHTML = ''; // Limpia la fila antes de añadir las mesas
  
//         if (state[rowIndex]) { // Verifica que la fila exista en el estado guardado
//           state[rowIndex].forEach((mesaState, mesaIndex) => {
//             const mesa = document.createElement('div');
//             mesa.className = mesaState.class;
//             mesa.textContent = mesaState.content;
//             mesa.id = `user-mesa-${rowIndex}-${mesaIndex}`;  // Asegura un id único para cada mesa en la vista de usuario
//             mesa.setAttribute('draggable', false);
//             row.appendChild(mesa);
//           });
//         }
//       });
//     }
//   }
  
//   document.addEventListener('DOMContentLoaded', () => {
//     const mesas = document.querySelectorAll('.mesa');
//     mesas.forEach((mesa, index) => {
//       mesa.id = `mesa-${index}`;  // Asegura un id único para cada mesa
//     });
  
//     loadState();
//   });
  





// function allowDrop(ev) {
//   ev.preventDefault();
// }

// function drag(ev) {
//   ev.dataTransfer.setData("text", ev.target.id);
// }

// function drop(ev) {
//   ev.preventDefault();
//   const data = ev.dataTransfer.getData("text");
//   const draggedElement = document.getElementById(data);
//   const dropTarget = ev.target;

//   // Verifica que el objetivo de la caída no sea descendiente del elemento arrastrado
//   if (draggedElement && !draggedElement.contains(dropTarget) && (dropTarget.classList.contains('droppable') || dropTarget.classList.contains('mesa'))) {
//     dropTarget.appendChild(draggedElement);
//     updateUserView();
//   }
// }

// function updateUserView() {
//   const adminViewRows = document.querySelectorAll('#admin-view .row');
//   const userViewContainer = document.querySelector('#user-view');

//   // Asegúrate de que el número de filas en ambas vistas coincida
//   while (userViewContainer.children.length < adminViewRows.length) {
//     const newRow = document.createElement('div');
//     newRow.className = 'row';
//     userViewContainer.appendChild(newRow);
//   }

//   // Limpia las filas de la vista de usuario
//   Array.from(userViewContainer.children).forEach(row => {
//     row.innerHTML = '';
//   });

//   // Copia las mesas de la vista de administrador a la vista de usuario
//   adminViewRows.forEach((adminRow, rowIndex) => {
//     const userRow = userViewContainer.children[rowIndex];
//     adminRow.querySelectorAll('.mesa').forEach(mesa => {
//       const userMesa = mesa.cloneNode(true);
//       userMesa.id = ''; // Elimina el id para evitar duplicados
//       userMesa.setAttribute('draggable', false);
//       userRow.appendChild(userMesa);
//     });
//   });
// }

// document.addEventListener('DOMContentLoaded', () => {
//   const mesas = document.querySelectorAll('.mesa');
//   mesas.forEach((mesa, index) => {
//     mesa.id = `mesa-${index}`;  // Asegura un id único para cada mesa
//   });

//   updateUserView();
// });
