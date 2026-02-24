# Diagram Templates (Mermaid.js)

Use these Mermaid.js templates to generate professional diagrams for the Appendices of the System Description.

**How to Use**: Copy the code block into a Markdown viewer that supports Mermaid (like GitHub, Notion, or specialized editors) to render the visual.

---

## Appendix B: System Architecture Diagram

This diagram shows the high-level components of a typical SaaS application on AWS.

```mermaid
graph TB
    subgraph "Corporate Environment"
        Emp[Employees]
        Dev[Developers]
    end

    subgraph "Customer Environment"
        User[End Users]
        Admin[Admin Users]
    end

    subgraph "AWS Cloud (Production VPC)"
        LB[Load Balancer]
        
        subgraph "App Layer"
            App1[App Server 1]
            App2[App Server 2]
        end
        
        subgraph "Data Layer"
            DB[(RDS Database)]
            Cache[(Redis Cache)]
            S3[(S3 Storage)]
        end
    end

    User -->|HTTPS| LB
    Admin -->|HTTPS| LB
    
    LB --> App1
    LB --> App2
    
    App1 --> DB
    App1 --> Cache
    App1 --> S3
    App2 --> DB
    
    Dev -->|VPN/SSO| AWS[AWS Console]
```

---

## Appendix C: Network Diagram

This diagram illustrates network segmentation, subnets, and security groups.

```mermaid
graph TB
    subgraph "Internet"
        Gateway[Internet Gateway]
    end

    subgraph "VPC (10.0.0.0/16)"
        
        subgraph "Public Subnet"
            NAT[NAT Gateway]
            ALB[Application Load Balancer]
            Bastion[Bastion Host / VPN]
        end
        
        subgraph "Private Subnet (App)"
            ECS[ECS Cluster / App Servers]
        end
        
        subgraph "Private Subnet (Data)"
            RDS[(RDS Primary)]
            RDS_Replica[(RDS Replica)]
        end
    end

    Gateway --> ALB
    Gateway --> Bastion
    
    ALB -->|Port 443| ECS
    Bastion -->|SSH/VPN| ECS
    
    ECS -->|SQL:5432| RDS
    ECS -->|Outbound| NAT
    
    RDS -.->|Replication| RDS_Replica
```

---

## Appendix D: Data Flow Diagram

This diagram shows how customer data flows through the system, from entry to storage.

```mermaid
sequenceDiagram
    participant User as Customer
    participant API as API Gateway/WAF
    participant App as Application Service
    participant DB as Database (Encrypted)
    participant S3 as File Storage (Encrypted)
    participant Log as Logging Service

    User->>API: 1. Submit Data (HTTPS/TLS 1.2)
    Note right of User: Data Entry
    
    API->>API: 2. Validate & Auth
    API->>App: 3. Forward Request
    
    App->>App: 4. Process Data
    Note right of App: Data Processing
    
    App->>DB: 5. Store Structured Data (AES-256)
    App->>S3: 6. Store Files/Uploads (AES-256)
    Note right of DB: Data Storage
    
    App-->>Log: 7. Log Metadata (No PII)
    
    App-->>User: 8. Success Response
```

