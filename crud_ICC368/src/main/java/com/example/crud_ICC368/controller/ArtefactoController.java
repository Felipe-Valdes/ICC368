package com.example.crud_ICC368.controller;


import com.example.crud_ICC368.entity.Artefacto;
import com.example.crud_ICC368.service.ArtefactoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/artefactos")
public class ArtefactoController {
    @Autowired
    private ArtefactoService artefactoService;

    @GetMapping
    public List<Artefacto> listar() {
        return artefactoService.listarTodos();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Artefacto> obtenerPorId(@PathVariable Long id) {
        return artefactoService.obtenerPorId(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public Artefacto crear(@RequestBody Artefacto artefacto) {
        return artefactoService.guardar(artefacto);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Artefacto> actualizar(@PathVariable Long id, @RequestBody Artefacto artefacto) {
        if (!artefactoService.obtenerPorId(id).isPresent()) {
            return ResponseEntity.notFound().build();
        }
        artefacto.setId(id);
        return ResponseEntity.ok(artefactoService.guardar(artefacto));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> eliminar(@PathVariable Long id) {
        if (!artefactoService.obtenerPorId(id).isPresent()) {
            return ResponseEntity.notFound().build();
        }
        artefactoService.eliminar(id);
        return ResponseEntity.noContent().build();
    }

}
