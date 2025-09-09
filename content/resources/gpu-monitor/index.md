---
title: "GPU Usage Monitor"
date: 2025-01-09
summary: "Real-time GPU usage monitoring for lab servers"
---

<div id="gpu-monitor-container">
  <div style="text-align: center; margin-bottom: 2rem;">
    <h1 style="color: #1f2937; margin-bottom: 0.5rem;">🖥️ GPU Usage Monitor</h1>
    <p style="color: #6b7280; font-size: 1.1rem;">Real-time monitoring of lab GPU resources</p>
    <div id="last-updated" style="color: #9ca3af; font-size: 0.9rem; margin-top: 1rem;">
      Last updated: <span id="update-time">Loading...</span>
    </div>
  </div>

  <div id="loading" style="text-align: center; padding: 2rem;">
    <div style="font-size: 1.2rem; color: #6b7280;">🔄 Loading GPU data...</div>
  </div>

  <div id="error-message" style="display: none; text-align: center; padding: 2rem; background-color: #fef2f2; border: 1px solid #fecaca; border-radius: 8px; margin: 1rem 0;">
    <div style="color: #dc2626; font-size: 1.1rem;">❌ Failed to load GPU data</div>
    <div style="color: #7f1d1d; font-size: 0.9rem; margin-top: 0.5rem;" id="error-details"></div>
  </div>

  <div id="servers-container" style="display: none;">
    <!-- GPU cards will be dynamically inserted here -->
  </div>

  <div style="text-align: center; margin-top: 2rem;">
    <button id="refresh-btn" onclick="loadGPUData()" 
            style="background-color: #3b82f6; color: white; padding: 0.75rem 1.5rem; border: none; border-radius: 8px; font-size: 1rem; cursor: pointer; transition: background-color 0.2s;">
      🔄 Refresh Data
    </button>
  </div>
</div>

<style>
.server-card {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  padding: 1.5rem;
  margin-bottom: 2rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.server-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #e5e7eb;
}

.server-title {
  font-size: 1.4rem;
  font-weight: 600;
  color: #1f2937;
}

.server-summary {
  background-color: #f3f4f6;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-size: 0.9rem;
  color: #374151;
}

.gpu-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1rem;
}

.gpu-card {
  border: 1px solid #d1d5db;
  border-radius: 8px;
  padding: 1rem;
  background-color: #fafafa;
}

.gpu-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.gpu-name {
  font-weight: 600;
  color: #374151;
  font-size: 0.9rem;
}

.gpu-id {
  background-color: #e5e7eb;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-size: 0.8rem;
  color: #6b7280;
}

.usage-bars {
  margin-bottom: 1rem;
}

.usage-bar {
  margin-bottom: 0.75rem;
}

.usage-label {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.25rem;
  font-size: 0.85rem;
  color: #4b5563;
}

.progress-bar {
  width: 100%;
  height: 8px;
  background-color: #e5e7eb;
  border-radius: 4px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  transition: width 0.3s ease;
  border-radius: 4px;
}

.utilization-low { background-color: #10b981; }
.utilization-medium { background-color: #f59e0b; }
.utilization-high { background-color: #ef4444; }

.memory-low { background-color: #06b6d4; }
.memory-medium { background-color: #f59e0b; }
.memory-high { background-color: #ef4444; }

.gpu-stats {
  display: flex;
  justify-content: space-between;
  font-size: 0.8rem;
  color: #6b7280;
}

#refresh-btn:hover {
  background-color: #2563eb;
}

.status-indicator {
  display: inline-block;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  margin-right: 0.5rem;
}

.status-success { background-color: #10b981; }
.status-error { background-color: #ef4444; }
</style>

<script>
const API_ENDPOINT = 'http://58.56.75.202:8000/api/gpu_status';

function getUtilizationClass(utilization) {
  if (utilization < 30) return 'utilization-low';
  if (utilization < 70) return 'utilization-medium';
  return 'utilization-high';
}

function getMemoryClass(percentage) {
  if (percentage < 50) return 'memory-low';
  if (percentage < 80) return 'memory-medium';
  return 'memory-high';
}

function formatMemory(mb) {
  if (mb >= 1024) {
    return (mb / 1024).toFixed(1) + ' GB';
  }
  return mb.toFixed(0) + ' MB';
}

function createGPUCard(gpu) {
  const memoryPercentage = (gpu.mem_used / gpu.mem_total) * 100;
  
  return `
    <div class="gpu-card">
      <div class="gpu-header">
        <div class="gpu-name">GPU ${gpu.id}</div>
        <div class="gpu-id">${gpu.name}</div>
      </div>
      
      <div class="usage-bars">
        <div class="usage-bar">
          <div class="usage-label">
            <span>Utilization</span>
            <span><strong>${gpu.utilization.toFixed(1)}%</strong></span>
          </div>
          <div class="progress-bar">
            <div class="progress-fill ${getUtilizationClass(gpu.utilization)}" 
                 style="width: ${gpu.utilization}%"></div>
          </div>
        </div>
        
        <div class="usage-bar">
          <div class="usage-label">
            <span>Memory</span>
            <span><strong>${memoryPercentage.toFixed(1)}%</strong></span>
          </div>
          <div class="progress-bar">
            <div class="progress-fill ${getMemoryClass(memoryPercentage)}" 
                 style="width: ${memoryPercentage}%"></div>
          </div>
        </div>
      </div>
      
      <div class="gpu-stats">
        <span>Used: ${formatMemory(gpu.mem_used)}</span>
        <span>Total: ${formatMemory(gpu.mem_total)}</span>
      </div>
    </div>
  `;
}

function createServerCard(serverData) {
  const { hostname, port, status, gpus, summary } = serverData;
  const isOnline = status === 'success';
  
  let content = `
    <div class="server-card">
      <div class="server-header">
        <div>
          <div class="server-title">
            <span class="status-indicator ${isOnline ? 'status-success' : 'status-error'}"></span>
            ${hostname}:${port}
          </div>
        </div>
        <div class="server-summary">
          ${isOnline ? `${summary.used}/${summary.total} GPUs Online` : 'Server Offline'}
        </div>
      </div>
  `;
  
  if (isOnline && gpus && gpus.length > 0) {
    content += `
      <div class="gpu-grid">
        ${gpus.map(gpu => createGPUCard(gpu)).join('')}
      </div>
    `;
  } else if (!isOnline) {
    content += `
      <div style="text-align: center; padding: 2rem; color: #6b7280;">
        <div style="font-size: 1.1rem;">⚠️ Server is currently offline</div>
        <div style="font-size: 0.9rem; margin-top: 0.5rem;">Unable to retrieve GPU information</div>
      </div>
    `;
  }
  
  content += '</div>';
  return content;
}

async function loadGPUData() {
  const loadingEl = document.getElementById('loading');
  const errorEl = document.getElementById('error-message');
  const containersEl = document.getElementById('servers-container');
  const updateTimeEl = document.getElementById('update-time');
  const refreshBtn = document.getElementById('refresh-btn');
  
  loadingEl.style.display = 'block';
  errorEl.style.display = 'none';
  containersEl.style.display = 'none';
  refreshBtn.disabled = true;
  refreshBtn.style.backgroundColor = '#9ca3af';
  
  try {
    const response = await fetch(API_ENDPOINT);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    
    const servers = Array.isArray(data) ? data : [data];
    
    loadingEl.style.display = 'none';
    containersEl.innerHTML = servers.map(server => createServerCard(server)).join('');
    containersEl.style.display = 'block';
    
    const now = new Date();
    updateTimeEl.textContent = now.toLocaleString();
    
  } catch (error) {
    console.error('Error loading GPU data:', error);
    loadingEl.style.display = 'none';
    errorEl.style.display = 'block';
    document.getElementById('error-details').textContent = error.message;
  } finally {
    refreshBtn.disabled = false;
    refreshBtn.style.backgroundColor = '#3b82f6';
  }
}

document.addEventListener('DOMContentLoaded', function() {
  loadGPUData();
  setInterval(loadGPUData, 30000);
});
</script>
