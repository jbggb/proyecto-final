from django.db import models

# Create your models here.  

#modelo pedido 
class Pedidos(models.Model):
    id_administrador = models.ForeignKey('administrador.Administradores', on_delete=models.CASCADE)
    id_cliente = models.ForeignKey('cliente.Clientes', on_delete=models.CASCADE)
    fecha_pedido = models.DateField()
    estado_pedido = models.CharField(max_length=150)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Pedido {self.id} - {self.estado_pedido} - total: {self.total}"
    
    
    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ['-fecha_pedido']
        
        def __str__(self):
            return f"Pedido {self.id} - {self.estado_pedido} - total: {self.total}"
        
            
        
        
            
        
    
    

        
    
    