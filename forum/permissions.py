from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """"Apenas o autor do post/comentario pode editar/deletar"""

    def has_object_permission(self, request, view, obj):
        """"A permissão de leitura é valida para qualquer pessoa"""
        if request.method in permissions.SAFE_METHODS:
            return True
        # A escrita é valida para autor e administrador
        return obj.author == request.user or request.user.is_staff

