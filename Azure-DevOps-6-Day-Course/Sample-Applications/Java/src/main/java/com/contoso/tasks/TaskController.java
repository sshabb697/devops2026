package com.contoso.tasks;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.concurrent.atomic.AtomicInteger;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TaskController {

    public record TaskItem(int id, String title, boolean done) {
    }

    public record NewTask(String title) {
    }

    private final List<TaskItem> tasks = new ArrayList<>(List.of(
            new TaskItem(1, "Learn Azure DevOps", false)));
    private final AtomicInteger nextId = new AtomicInteger(2);

    @GetMapping("/")
    public Map<String, String> index() {
        return Map.of("message", "Welcome to the Contoso Tasks API");
    }

    @GetMapping("/health")
    public Map<String, String> health() {
        return Map.of("status", "ok");
    }

    @GetMapping("/tasks")
    public List<TaskItem> listTasks() {
        return tasks;
    }

    @PostMapping("/tasks")
    public ResponseEntity<?> addTask(@RequestBody NewTask input) {
        String title = input.title() == null ? "" : input.title().trim();
        if (title.isEmpty()) {
            return ResponseEntity.badRequest().body(Map.of("error", "title is required"));
        }
        TaskItem task = new TaskItem(nextId.getAndIncrement(), title, false);
        tasks.add(task);
        return ResponseEntity.status(201).body(task);
    }
}
