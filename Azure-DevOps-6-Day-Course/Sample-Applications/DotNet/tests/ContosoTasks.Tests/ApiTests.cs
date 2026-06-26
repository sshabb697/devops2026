using System.Net;
using System.Net.Http.Json;
using Microsoft.AspNetCore.Mvc.Testing;
using Xunit;

public class ApiTests : IClassFixture<WebApplicationFactory<Program>>
{
    private readonly HttpClient _client;

    public ApiTests(WebApplicationFactory<Program> factory)
    {
        _client = factory.CreateClient();
    }

    [Fact]
    public async Task Health_Returns_Ok()
    {
        var response = await _client.GetAsync("/health");
        response.EnsureSuccessStatusCode();
        var body = await response.Content.ReadFromJsonAsync<HealthResponse>();
        Assert.Equal("ok", body!.Status);
    }

    [Fact]
    public async Task Get_Tasks_Returns_List()
    {
        var response = await _client.GetAsync("/tasks");
        response.EnsureSuccessStatusCode();
        var tasks = await response.Content.ReadFromJsonAsync<List<TaskItem>>();
        Assert.NotNull(tasks);
        Assert.NotEmpty(tasks!);
    }

    [Fact]
    public async Task Post_Task_Creates_Task()
    {
        var response = await _client.PostAsJsonAsync("/tasks", new { title = "Write tests" });
        Assert.Equal(HttpStatusCode.Created, response.StatusCode);
        var task = await response.Content.ReadFromJsonAsync<TaskItem>();
        Assert.Equal("Write tests", task!.Title);
        Assert.False(task.Done);
    }

    [Fact]
    public async Task Post_Task_Rejects_Empty_Title()
    {
        var response = await _client.PostAsJsonAsync("/tasks", new { title = "" });
        Assert.Equal(HttpStatusCode.BadRequest, response.StatusCode);
    }

    private record HealthResponse(string Status);
}
