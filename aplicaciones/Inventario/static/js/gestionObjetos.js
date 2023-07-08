(function(){
const btnEliminacion = document.querySelectorAll(".btnEliminacion");

btnEliminacion.forEach(btn => {
    btn.addEventListener('click',(e)=>{
        const confirmacion = confirm('¿Estás seguro de eliminar el registro?');
        if(!confirmacion){
            e.preventDefault();
        }
    });
});
})();

