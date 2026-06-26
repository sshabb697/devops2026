var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

// In-memory task store (resets on restart) — fine for a demo.
var tasks = new List<TaskItem> { new(1, "Learn Azure DevOps", false) };
var nextId = 2;

app.MapGet("/", () => Results.Ok(new { message = "Welcome to the Contoso Tasks API" }));

app.MapGet("/health", () => Results.Ok(new { status = "ok" }));

app.MapGet("/tasks", () => Results.Ok(tasks));

app.MapPost("/tasks", (NewTask input) =>
{
    var title = (input.Title ?? string.Empty).Trim();
    if (string.IsNullOrEmpty(title))
    {
        return Results.BadRequest(new { error = "title is required" });
    }

    var task = new TaskItem(nextId++, title, false);
    tasks.Add(task);
    return Results.Created($"/tasks/{task.Id}", task);
});

app.Run();

public record TaskItem(int Id, string Title, bool Done);
public record NewTask(string? Title);

// Exposed so the test project can use WebApplicationFactory<Program>.
public partial class Program { }
